(function(){
"use strict";
var slides=Array.prototype.slice.call(document.querySelectorAll('.slide-wrapper'));
var mode='slide', aud='all', track=[], cur=0;
var AUDLABEL={all:(document.body.dataset.deckLabel||'Complete Deck'),mgmt:'Management View',arch:"Architect's View"};
function audOk(s){if(aud==='all')return true;var a=s.dataset.aud;return a==='exec'||a===aud;}
function searchOk(s){var q=(document.getElementById('sidebarSearch').value||'').toLowerCase().trim();if(!q)return true;return (s.dataset.num+' '+s.dataset.title+' '+s.dataset.tag+' '+s.dataset.chapter).toLowerCase().indexOf(q)>-1;}
function rebuild(){
  track=slides.filter(function(s){return audOk(s)&&searchOk(s);});
  slides.forEach(function(s){s.classList.toggle('in-track',track.indexOf(s)>-1);});
  var sel=document.getElementById('ctrlJumpSelect');sel.innerHTML='';
  track.forEach(function(s,i){var o=document.createElement('option');o.value=i;o.textContent=s.dataset.num+' '+s.dataset.title;sel.appendChild(o);});
  renderSidebar();
}
function pill(a){if(a==='mgmt')return '<span class="status-pill status-warning">MGMT</span>';if(a==='arch')return '<span class="status-pill status-danger">ARCH</span>';return '<span class="status-pill status-success">EXEC &amp; TECH</span>';}
function renderSidebar(){
  var ul=document.getElementById('sidebarMenuList');ul.innerHTML='';var last='';
  track.forEach(function(s,i){
    if(s.dataset.chapter!==last){var h=document.createElement('li');h.className='sidebar-category-header';h.textContent=s.dataset.chapter;ul.appendChild(h);last=s.dataset.chapter;}
    var li=document.createElement('li');li.className='sidebar-item'+(i===cur?' active':'');li.tabIndex=0;li.setAttribute('role','button');
    li.innerHTML='<div class="sidebar-item-header"><span class="num-badge">'+s.dataset.num+'</span>'+pill(s.dataset.aud)+'</div><span class="sidebar-item-title">'+s.dataset.title+'</span>';
    li.onclick=function(){go(i,true);};li.onkeydown=function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();go(i,true);}};
    ul.appendChild(li);
  });
}
function updateChrome(){
  var n=track.length, s=track[cur];
  document.getElementById('ctrlSlideCounter').textContent=n?('Slide '+(cur+1)+' of '+n):'No slides';
  document.getElementById('ctrlProgressBar').style.width=(n?Math.round((cur+1)/n*100):0)+'%';
  document.getElementById('ctrlPrevBtn').disabled=cur<=0;
  document.getElementById('ctrlNextBtn').disabled=cur>=n-1;
  document.getElementById('ctrlJumpSelect').value=cur;
  document.getElementById('ribbonSlideTitle').textContent=s?(s.dataset.num+' '+s.dataset.title+' ('+(cur+1)+' of '+n+')'):'';
  var p=document.getElementById('ribbonViewPill');p.className='pill-badge pill-'+aud;p.textContent=AUDLABEL[aud]+' ('+n+' slides)';
  document.querySelectorAll('#sidebarMenuList .sidebar-item').forEach(function(li,i){li.classList.toggle('active',i===cur);if(i===cur){var sb=document.querySelector('aside.sidebar-nav');var lt=li.offsetTop, lb=lt+li.offsetHeight;if(lt<sb.scrollTop+90||lb>sb.scrollTop+sb.clientHeight-10){sb.scrollTop=Math.max(0,lt-sb.clientHeight/3);}}});
}
function go(i,fromNav){
  if(!track.length)return;
  cur=Math.max(0,Math.min(i,track.length-1));
  var stage=document.getElementById('stage');
  if(mode==='full'){
    if(fromNav!==false){lockSpy=true;track[cur].scrollIntoView({behavior:'smooth',block:'start'});setTimeout(function(){lockSpy=false;},700);}
  }else{
    slides.forEach(function(s){s.classList.remove('show');});
    track[cur].classList.add('show');stage.scrollTop=0;document.documentElement.scrollTop=0;document.body.scrollTop=0;
  }
  updateChrome();
}
window.stepSlide=function(d){go(cur+d,true);};
window.jumpToSlide=function(v){go(parseInt(v,10),true);};
window.setAudience=function(a){
  var keep=track[cur];aud=a;
  document.querySelectorAll('.aud-btn').forEach(function(b){b.classList.toggle('active',b.dataset.aud===a);});
  rebuild();var k=track.indexOf(keep);go(k>-1?k:0,true);
};
window.filterSidebarSlides=function(){var keep=track[cur];rebuild();var k=track.indexOf(keep);go(k>-1?k:0,true);};
function setTabs(){document.querySelectorAll('.view-btn').forEach(function(b){b.classList.toggle('active',b.dataset.mode===mode);});}
window.setMode=function(m){
  if(m==='present'){enterPresent();return;}
  if(mode==='present'){exitFs();}
  mode=m;document.body.classList.remove('present-mode');document.documentElement.classList.remove('present-root');
  document.body.classList.toggle('full-mode',m==='full');
  slides.forEach(function(s){s.classList.remove('show');});
  setTabs();
  if(m==='full'){setTimeout(function(){go(cur,true);},30);}else{go(cur,false);}
};
function enterPresent(){
  mode='present';document.body.classList.remove('full-mode');document.body.classList.add('present-mode');document.documentElement.classList.add('present-root');setTabs();go(cur,false);
  var el=document.documentElement;
  try{if(el.requestFullscreen&&!document.fullscreenElement){el.requestFullscreen().catch(function(){});}}catch(e){}
}
function exitFs(){try{if(document.fullscreenElement&&document.exitFullscreen){document.exitFullscreen().catch(function(){});}}catch(e){}}
window.exitPresent=function(){setMode('slide');};
document.addEventListener('fullscreenchange',function(){if(!document.fullscreenElement&&mode==='present'){setMode('slide');}});
window.toggleDarkMode=function(){document.body.classList.toggle('dark-mode');};
window.toggleNotes=function(){var on=document.body.classList.toggle('notes-on');document.getElementById('btnNotes').classList.toggle('on',on);};
/* scroll spy for full view */
var lockSpy=false;
document.getElementById('stage').addEventListener('scroll',function(){
  if(mode!=='full'||lockSpy)return;
  var st=this.getBoundingClientRect().top, best=0;
  track.forEach(function(s,i){if(s.getBoundingClientRect().top-st<160)best=i;});
  if(best!==cur){cur=best;updateChrome();}
},{passive:true});
document.addEventListener('keydown',function(e){
  var t=e.target.tagName;if(t==='INPUT'||t==='SELECT'||t==='TEXTAREA')return;
  if(e.key==='ArrowRight'||e.key==='PageDown'||(e.key===' '&&mode!=='full')){e.preventDefault();stepSlide(1);}
  else if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();stepSlide(-1);}
  else if(e.key==='Home'){e.preventDefault();go(0,true);}
  else if(e.key==='End'){e.preventDefault();go(track.length-1,true);}
  else if(e.key==='f'||e.key==='F'){e.preventDefault();if(mode==='present')setMode('slide');else setMode('present');}
  else if(e.key==='Escape'&&mode==='present'){setMode('slide');}
  else if(e.key==='n'||e.key==='N'){toggleNotes();}
});
window.addEventListener('beforeprint',function(){document.body.classList.add('printing');});
/* draggable controller */
(function(){
  var pane=document.getElementById('frozenPane');var drag=false,sx,sy,il,it;
  pane.addEventListener('pointerdown',function(e){
    if(e.target.closest('button')||e.target.closest('select'))return;
    drag=true;sx=e.clientX;sy=e.clientY;var r=pane.getBoundingClientRect();il=r.left;it=r.top;
    pane.style.bottom='auto';pane.style.right='auto';pane.style.left=il+'px';pane.style.top=it+'px';pane.style.cursor='grabbing';
    document.addEventListener('pointermove',mv);document.addEventListener('pointerup',up);
  });
  function mv(e){if(!drag)return;var nl=il+e.clientX-sx,nt=it+e.clientY-sy;
    nl=Math.max(10,Math.min(nl,window.innerWidth-pane.offsetWidth-10));nt=Math.max(10,Math.min(nt,window.innerHeight-pane.offsetHeight-10));
    pane.style.left=nl+'px';pane.style.top=nt+'px';}
  function up(){drag=false;pane.style.cursor='grab';document.removeEventListener('pointermove',mv);document.removeEventListener('pointerup',up);}
})();
rebuild();go(0,false);
})();
