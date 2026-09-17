<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>EMOM Timer</title>
<style>
:root{
  --bg:#0b0e14;
  --panel:#161c26;
  --line:#2a3342;
  --text:#f2f5f9;
  --dim:#8b94a3;
  --accent:#4da3ff;
  --amber:#ffb020;
  --red:#ff453a;
  --green:#30d158;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%}
body{
  background:var(--bg);
  color:var(--text);
  overflow:hidden;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-user-select:none;user-select:none;
  -webkit-touch-callout:none;
}

/* ---- top progress bar ---- */
#progressWrap{position:fixed;top:0;left:0;right:0;height:12px;background:#1a2130;z-index:40}
#progressBar{height:100%;width:0%;background:var(--accent)}

/* ---- header / corner info ---- */
header{
  position:fixed;top:12px;left:0;right:0;
  display:flex;justify-content:space-between;align-items:center;
  padding:calc(12px + env(safe-area-inset-top)) 18px 0;
  font-size:13px;color:var(--dim);letter-spacing:.06em;z-index:41;pointer-events:none;
}
.corner{display:flex;flex-direction:column;align-items:flex-start;gap:4px}
#elapsedBox,#remainingBox{font-size:26px} /* 2x the old 13px */
#elapsedBox b,#remainingBox b{
  color:var(--text);font-weight:600;
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-variant-numeric:tabular-nums;
}
#wakeNote{display:none;color:var(--amber)}

/* ---- layout ---- */
main{
  position:absolute;inset:0;
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:24px;padding:28px;text-align:center;
}
section[hidden]{display:none !important}

/* ---- setup screen ---- */
h1{font-size:clamp(1.3rem,4vw,2rem);letter-spacing:.28em;font-weight:700;color:var(--text)}
.card{
  background:var(--panel);border:1px solid var(--line);border-radius:16px;
  padding:22px 24px;display:flex;flex-direction:column;gap:20px;width:min(92vw,380px);
}
.row{display:flex;align-items:center;justify-content:space-between;gap:14px}
.row label{font-size:.95rem;color:var(--dim);letter-spacing:.05em}
input[type=number]{
  width:84px;padding:8px 10px;font-size:1.5rem;text-align:center;
  background:var(--bg);color:var(--text);border:1px solid var(--line);border-radius:10px;
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
input[type=range]{flex:1;accent-color:var(--accent);height:28px}
input[type=checkbox]{width:22px;height:22px;accent-color:var(--accent)}
.muteRow{display:flex;align-items:center;gap:10px}
.muteRow span{font-size:.95rem;color:var(--dim);letter-spacing:.05em}

/* ---- buttons ---- */
.btn{
  border:1px solid var(--line);border-radius:14px;background:var(--panel);color:var(--text);
  font-size:1.05rem;padding:14px 28px;cursor:pointer;touch-action:manipulation;
  font-family:inherit;letter-spacing:.04em;
}
.btn:active{transform:scale(.97)}
#startBtn{
  background:var(--accent);color:#06121f;border:none;font-weight:700;
  font-size:1.3rem;padding:18px 64px;border-radius:16px;letter-spacing:.1em;
}
.controls{display:flex;align-items:center;gap:22px}

/* ---- hold-to-reset button with fill ring ---- */
.holdBtn{
  position:relative;width:76px;height:76px;border-radius:50%;
  background:var(--panel);border:1px solid var(--line);color:var(--dim);
  font-size:10px;letter-spacing:.1em;cursor:pointer;touch-action:none;font-family:inherit;
}
.holdBtn .ring{
  position:absolute;inset:-7px;border-radius:50%;pointer-events:none;
  background:conic-gradient(var(--accent) calc(var(--p,0)*1turn), rgba(255,255,255,.07) 0);
  -webkit-mask:radial-gradient(farthest-side,transparent calc(100% - 6px),#000 calc(100% - 5px));
          mask:radial-gradient(farthest-side,transparent calc(100% - 6px),#000 calc(100% - 5px));
}

/* ---- timer screen ---- */
#digits{
  font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  font-variant-numeric:tabular-nums;
  font-size:clamp(5rem,32vw,18rem);
  line-height:.95;font-weight:700;color:var(--text);
}
#digits.amber{color:var(--amber)}
#digits.red{color:var(--red)}
#readyHint{
  display:none;font-size:clamp(1rem,3.5vw,1.6rem);letter-spacing:.35em;color:var(--amber);font-weight:700;
}
#roundLabel{
  font-size:clamp(1.1rem,4vw,1.8rem);letter-spacing:.3em;color:var(--dim);font-weight:600;
}

/* ---- paused overlay ---- */
#pausedOverlay{
  position:fixed;inset:0;z-index:60;background:rgba(5,8,12,.84);
  display:flex;align-items:center;justify-content:center;
  font-size:clamp(3rem,16vw,9rem);font-weight:800;letter-spacing:.3em;color:var(--text);
  pointer-events:none; /* visual only: taps pass through to the Resume button */
}
#pausedOverlay[hidden]{display:none !important}

/* ---- complete screen ---- */
#doneWord{
  color:var(--green);font-size:clamp(4rem,20vw,12rem);font-weight:800;letter-spacing:.12em;line-height:1;
}
#finalStats{font-size:1.15rem;color:var(--dim);letter-spacing:.05em}
#finalStats b{color:var(--text)}
.hint{font-size:.9rem;color:var(--dim);opacity:.8}
</style>
</head>
<body>

<div id="progressWrap"><div id="progressBar"></div></div>

<header>
  <div class="corner">
    <span id="remainingBox">REMAINING <b id="remaining">10:00</b></span>
    <span id="wakeNote">&#9888; screen may sleep</span>
  </div>
  <span id="elapsedBox">ELAPSED <b id="elapsed">00:00</b></span>
</header>

<main>
  <!-- SETUP -->
  <section id="setupScreen">
    <h1 style="margin-bottom:24px">EMOM TIMER</h1>
    <div class="card">
      <div class="row">
        <label for="roundsInput">Rounds (1&ndash;99)</label>
        <input type="number" id="roundsInput" min="1" max="99" step="1" value="10">
      </div>
      <div class="row">
        <label for="volSlider">Volume</label>
        <input type="range" id="volSlider" min="0" max="100" step="1" value="80">
      </div>
      <div class="muteRow">
        <input type="checkbox" id="muteChk">
        <span for="muteChk">Mute (tones + voice)</span>
      </div>
    </div>
    <button class="btn" id="startBtn" style="margin-top:24px">START</button>
  </section>

  <!-- RUNNING / PAUSED -->
  <section id="timerScreen" hidden>
    <div id="digits">60</div>
    <div id="readyHint">GET READY</div>
    <div id="roundLabel">ROUND 1 / 10</div>
    <div class="controls" style="margin-top:32px">
      <button class="btn" id="pauseBtn">Pause</button>
      <button class="holdBtn" id="resetBtnTimer"><span class="ring"></span>RESET</button>
    </div>
  </section>

  <!-- COMPLETE -->
  <section id="completeScreen" hidden>
    <div id="doneWord">DONE</div>
    <div id="finalStats"></div>
    <div class="controls" style="margin-top:32px">
      <button class="holdBtn" id="resetBtnComplete"><span class="ring"></span>RESET</button>
    </div>
    <div class="hint">Hold RESET (~2s) to return to setup</div>
  </section>
</main>

<div id="pausedOverlay" hidden>PAUSED</div>

<script>
'use strict';

/* ================= constants & helpers ================= */
var ROUND_MS = 60000;          // fixed 60-second rounds
var LEAD_MS  = 2000;           // Round 1 lead-in after Start is pressed
var HOLD_MS  = 2000;           // hold-to-reset duration
var TTS_RATE = 1.1;            // brisk so the T-6s warning clears the ticks

function clampInt(v, lo, hi){ v = parseInt(v, 10); if (isNaN(v)) return lo; return Math.max(lo, Math.min(hi, v)); }
function fmtTime(ms){
  var s = Math.max(0, Math.floor(ms / 1000));
  var m = Math.floor(s / 60), r = s % 60;
  return (m < 10 ? '0' : '') + m + ':' + (r < 10 ? '0' : '') + r;
}
var ONES = ['zero','one','two','three','four','five','six','seven','eight','nine','ten',
            'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'];
var TENS = ['', '', 'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'];
function numToWords(n){
  if (n < 20) return ONES[n];
  var t = TENS[Math.floor(n / 10)], o = n % 10;
  return o ? t + '-' + ONES[o] : t;
}

/* ================= persistence (guarded) ================= */
function lsGet(k, d){ try { var v = localStorage.getItem(k); return v === null ? d : v; } catch (e) { return d; } }
function lsSet(k, v){ try { localStorage.setItem(k, String(v)); } catch (e) {} }

var totalRounds = clampInt(lsGet('emom.rounds', '10'), 1, 99);
var volume = parseFloat(lsGet('emom.volume', '0.8'));
if (!(volume >= 0 && volume <= 1)) volume = 0.8;
var muted = (lsGet('emom.muted', 'false') === 'true');

/* ================= DOM refs ================= */
var $ = function (id) { return document.getElementById(id); };
var setupScreen    = $('setupScreen');
var timerScreen    = $('timerScreen');
var completeScreen = $('completeScreen');
var pausedOverlay  = $('pausedOverlay');
var digits         = $('digits');
var readyHint      = $('readyHint');
var roundLabel     = $('roundLabel');
var progressBar    = $('progressBar');
var elapsedEl      = $('elapsed');
var remainingEl    = $('remaining');
var wakeNote       = $('wakeNote');
var roundsInput    = $('roundsInput');
var volSlider      = $('volSlider');
var muteChk        = $('muteChk');
var startBtn       = $('startBtn');
var pauseBtn       = $('pauseBtn');
var finalStats     = $('finalStats');

/* ================= state machine ================= */
var state = 'setup';           // setup | running | paused | complete
var currentRound = 1;
var roundStart = 0;            // epoch ms when the current round began
var pausedRemaining = ROUND_MS;
var prevRemaining = ROUND_MS;  // remaining (ms) at the previous tick, for cue crossing detection
var sawHidden = false;         // document went hidden since the last visible tick
var completionElapsed = 0;
var cues = { tts: false, round1: false };  // per-round cue flags

function resetCues(){ cues.tts = false; cues.round1 = false; }

/* ================= audio engine (Web Audio, synthesized) ================= */
var audioCtx = null, masterGain = null;

function ensureAudio(){
  if (!audioCtx){
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return false;
    try {
      audioCtx = new AC();
      masterGain = audioCtx.createGain();
      masterGain.connect(audioCtx.destination);
      applyVolume();
    } catch (e) { audioCtx = null; return false; }
  }
  if (audioCtx.state === 'suspended') audioCtx.resume().catch(function(){});
  return true;
}
function applyVolume(){
  if (masterGain) masterGain.gain.value = muted ? 0 : volume;
}
function tone(freq, durMs, peak, when, freqEnd){
  if (!audioCtx || !masterGain) return;
  try {
    var t = audioCtx.currentTime + (when || 0);
    var osc = audioCtx.createOscillator();
    var g = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(freq, t);
    if (freqEnd) osc.frequency.exponentialRampToValueAtTime(freqEnd, t + durMs / 1000);
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(peak, t + 0.012);
    g.gain.exponentialRampToValueAtTime(0.0001, t + durMs / 1000);
    osc.connect(g); g.connect(masterGain);
    osc.start(t);
    osc.stop(t + durMs / 1000 + 0.05);
  } catch (e) {}
}
function tickTone(){ tone(880, 80, 0.4, 0); }   // T-3/T-2/T-1 blip
// Round-start beep: prominent — louder (0.75 vs 0.5), longer (320ms), rising sweep E5->C6.
function beepTone(){ tone(660, 320, 0.75, 0, 1046.5); }
function fanfare(){                              // modest three-note chime, ~1s
  tone(523.25, 350, 0.45, 0);    // C5
  tone(659.25, 350, 0.45, 0.28); // E5
  tone(783.99, 520, 0.50, 0.56); // G5
}

/* ================= voice (Web Speech, degrades silently) ================= */
function speak(text){
  if (!('speechSynthesis' in window)) return;
  try {
    var synth = window.speechSynthesis;
    if (synth.speaking || synth.pending) synth.cancel(); // preempt any in-flight cue
    var u = new SpeechSynthesisUtterance(text);
    u.rate = TTS_RATE;
    u.volume = muted ? 0 : volume;
    synth.speak(u);
  } catch (e) {}
}
function stopSpeech(){
  if ('speechSynthesis' in window) { try { window.speechSynthesis.cancel(); } catch (e) {} }
}

/* ================= wake lock (graceful degradation) ================= */
var wakeSentinel = null;
function requestWakeLock(){
  if (!('wakeLock' in navigator)) { wakeNote.style.display = 'block'; return; }
  navigator.wakeLock.request('screen').then(function (sentinel) {
    wakeSentinel = sentinel;
    wakeNote.style.display = 'none';
    // UA releases the lock when the document is hidden; nothing to do here.
    sentinel.addEventListener('release', function () {});
  }).catch(function () {
    wakeNote.style.display = 'block';
  });
}
function releaseWakeLock(){
  if (wakeSentinel) {
    try { wakeSentinel.release().catch(function(){}); } catch (e) {}
    wakeSentinel = null;
  }
}

/* ================= timing engine (timestamp-based) ================= */
function tick(){
  if (state !== 'running') return;
  var now = Date.now();
  var cur = ROUND_MS - (now - roundStart);
  var delta = prevRemaining - cur;
  // Audible only when the tab has been continuously visible and ticking with a
  // small gap. A large gap or any hidden period since the last tick means cues
  // were missed -> skip them (no catch-up barrage); display shows current truth.
  var audible = !document.hidden && !sawHidden && delta >= 0 && delta < 500;

  if (cur <= 0) {
    // Minute boundary crossed. Catch up through ALL missed boundaries in one tick
    // (e.g., returning from a hidden tab) so the display never shows an
    // intermediate state. A T-0 beep fires only when exactly one recent
    // boundary was missed; missed-boundary cues are otherwise skipped.
    var firstMissedBy = -cur;
    var crossings = 0;
    while (cur <= 0) {
      if (currentRound >= totalRounds) { completeWorkout(); return; }
      currentRound++;
      roundStart += ROUND_MS;
      cur = ROUND_MS - (now - roundStart);
      resetCues();
      crossings++;
    }
    prevRemaining = cur;
    if (audible && crossings === 1 && firstMissedBy < 300) beepTone(); // T-0 beep for the new round
    renderTimer(cur);
    if (!document.hidden) sawHidden = false;
    return;
  }

  if (audible) {
    // Round 1 lead-in ends: beep + voice exactly as the round begins.
    if (!cues.round1 && prevRemaining > ROUND_MS && cur <= ROUND_MS) {
      beepTone();
      speak('Round one');
      cues.round1 = true;
    }
    var marks = [6, 3, 2, 1], i, m;
    for (i = 0; i < marks.length; i++) {
      m = marks[i] * 1000;
      if (prevRemaining > m && cur <= m) {
        if (marks[i] === 6) {
          // Advance warning: only when a next round exists (not on the final round).
          if (!cues.tts && currentRound < totalRounds) {
            speak('Round ' + numToWords(currentRound + 1) + ' starts in');
            cues.tts = true;
          }
        } else {
          tickTone();
        }
      }
    }
  }
  prevRemaining = cur;
  renderTimer(cur);
  if (!document.hidden) sawHidden = false;
}

/* ================= state transitions ================= */
function startWorkout(){
  totalRounds = clampInt(roundsInput.value, 1, 99);
  lsSet('emom.rounds', totalRounds);
  ensureAudio(); // user gesture: unlock AudioContext (autoplay policy)
  state = 'running';
  currentRound = 1;
  roundStart = Date.now() + LEAD_MS;   // 2s lead-in: the round itself starts later
  prevRemaining = ROUND_MS;
  resetCues();
  renderState();
  // Round 1's beep + "Round one" fire when the lead-in ends (see tick()).
  requestWakeLock();
}

function pauseWorkout(){
  if (state !== 'running') return;
  pausedRemaining = Math.max(0, ROUND_MS - (Date.now() - roundStart));
  state = 'paused';
  stopSpeech();
  if (audioCtx) audioCtx.suspend().catch(function(){}); // all audio silent while paused
  releaseWakeLock();
  renderState();
}

function resumeWorkout(){
  if (state !== 'paused') return;
  roundStart = Date.now() - (ROUND_MS - pausedRemaining); // continue exactly where it stopped
  state = 'running';
  prevRemaining = ROUND_MS - (Date.now() - roundStart);
  ensureAudio();
  requestWakeLock();
  // Paused inside the final 6s: voice fires immediately on resume only if >3s remain.
  if (pausedRemaining <= 6000 && pausedRemaining > 3000 && currentRound < totalRounds) {
    speak('Round ' + numToWords(currentRound + 1) + ' starts in');
    cues.tts = true;
  }
  renderState();
}

function completeWorkout(){
  // N rounds of exactly 60s each; the Round-1 lead-in is not workout time.
  completionElapsed = totalRounds * ROUND_MS;
  state = 'complete';
  releaseWakeLock();
  fanfare();
  speak('Workout complete');
  renderState();
}

function doReset(){
  state = 'setup';
  currentRound = 1;
  roundStart = 0;
  pausedRemaining = ROUND_MS; prevRemaining = ROUND_MS; completionElapsed = 0;
  resetCues();
  stopSpeech();
  releaseWakeLock();
  renderState();
}

/* ================= rendering ================= */
function renderTimer(cur){
  var sec = Math.max(0, Math.min(60, Math.ceil(cur / 1000)));
  digits.textContent = String(sec);
  readyHint.style.display = cur > ROUND_MS ? 'block' : 'none'; // visible during the lead-in
  digits.className = (sec <= 3) ? 'red' : (sec <= 10) ? 'amber' : '';
  roundLabel.textContent = 'ROUND ' + currentRound + ' / ' + totalRounds;
  var totalMs = totalRounds * ROUND_MS;
  // Elapsed is derived from round position, so the Round-1 lead-in never counts
  // and pausing can never produce negative time.
  var elapsedMs = Math.max(0, Math.min(totalMs, (currentRound - 1) * ROUND_MS + Math.max(0, ROUND_MS - cur)));
  elapsedEl.textContent = fmtTime(elapsedMs);
  remainingEl.textContent = fmtTime(totalMs - elapsedMs);
  progressBar.style.width = (elapsedMs / totalMs * 100) + '%';
}

function renderState(){
  setupScreen.hidden    = state !== 'setup';
  timerScreen.hidden    = !(state === 'running' || state === 'paused');
  completeScreen.hidden = state !== 'complete';
  pausedOverlay.hidden  = state !== 'paused';

  if (state === 'setup') {
    roundsInput.value = totalRounds;
    elapsedEl.textContent = '00:00';
    remainingEl.textContent = fmtTime(totalRounds * ROUND_MS);
    progressBar.style.width = '0%';
  } else if (state === 'running' || state === 'paused') {
    pauseBtn.textContent = (state === 'paused') ? 'Resume' : 'Pause';
    if (state === 'paused') renderTimer(pausedRemaining); // frozen numerals + times
  } else if (state === 'complete') {
    finalStats.innerHTML = 'Total time <b>' + fmtTime(completionElapsed) + '</b> &nbsp;&middot;&nbsp; Rounds <b>' + totalRounds + '/' + totalRounds + '</b>';
    elapsedEl.textContent = fmtTime(completionElapsed);
    remainingEl.textContent = '00:00';
    progressBar.style.width = '100%';
  }
}

/* ================= hold-to-reset (~2s, fill ring) ================= */
function attachHold(btn){
  var ring = btn.querySelector('.ring');
  var holding = false, holdStart = 0, rafId = 0;
  function stop(){
    if (!holding && !rafId) return;
    holding = false;
    cancelAnimationFrame(rafId);
    rafId = 0;
    ring.style.setProperty('--p', '0');
  }
  function step(){
    if (!holding) return;
    var p = Math.min(1, (performance.now() - holdStart) / HOLD_MS);
    ring.style.setProperty('--p', String(p));
    if (p >= 1) { stop(); doReset(); return; }
    rafId = requestAnimationFrame(step);
  }
  btn.addEventListener('pointerdown', function (e) {
    e.preventDefault();
    try { btn.setPointerCapture(e.pointerId); } catch (err) {}
    holding = true;
    holdStart = performance.now();
    rafId = requestAnimationFrame(step);
  });
  ['pointerup', 'pointercancel', 'lostpointercapture'].forEach(function (ev) {
    btn.addEventListener(ev, stop);
  });
  btn.addEventListener('contextmenu', function (e) { e.preventDefault(); }); // long-press on mobile
}

/* ================= wiring ================= */
startBtn.addEventListener('click', startWorkout);
pauseBtn.addEventListener('click', function () {
  if (state === 'running') pauseWorkout();
  else if (state === 'paused') resumeWorkout();
});
attachHold($('resetBtnTimer'));
attachHold($('resetBtnComplete'));

roundsInput.addEventListener('change', function () {
  totalRounds = clampInt(roundsInput.value, 1, 99);
  roundsInput.value = totalRounds;
  lsSet('emom.rounds', totalRounds);
});
volSlider.addEventListener('input', function () {
  volume = volSlider.value / 100;
  lsSet('emom.volume', volume);
  applyVolume();
});
muteChk.addEventListener('change', function () {
  muted = muteChk.checked;
  lsSet('emom.muted', muted);
  applyVolume();
});

/* Returning to the tab: recompute from timestamps (no catch-up audio), re-acquire wake lock. */
document.addEventListener('visibilitychange', function () {
  if (document.visibilityState === 'hidden') {
    sawHidden = true;
  } else if (state === 'running') {
    requestWakeLock();
    tick();
  }
});

/* ================= main loop: rAF + hidden-tab fallback ================= */
(function frame(){
  if (state === 'running') tick();
  requestAnimationFrame(frame);
})();
setInterval(function () { if (state === 'running') tick(); }, 250);

/* ================= init from persisted settings ================= */
roundsInput.value = totalRounds;
volSlider.value = Math.round(volume * 100);
muteChk.checked = muted;
if (!('wakeLock' in navigator)) wakeNote.style.display = 'block';
renderState();
</script>
</body>
</html>
