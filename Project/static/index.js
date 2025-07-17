// static/index.js

const api = location.origin;

async function callPow() {
  const base = +document.getElementById('pow-base').value;
  const exponent = +document.getElementById('pow-exp').value;
  const r = await fetch(api + '/math/pow', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({ base, exponent })
  });
  document.getElementById('pow-res').textContent =
    'Result: ' + (await r.json()).result;
}

async function callFib() {
  const n = +document.getElementById('fib-n').value;
  const r = await fetch(`${api}/math/fib/${n}`);
  document.getElementById('fib-res').textContent =
    'Result: ' + (await r.json()).result;
}

async function callFac() {
  const n = +document.getElementById('fac-n').value;
  const r = await fetch(`${api}/math/fact/${n}`);
  document.getElementById('fac-res').textContent =
    'Result: ' + (await r.json()).result;
}

// Optionally, you can export functions or attach them to window:
window.callPow = callPow;
window.callFib = callFib;
window.callFac = callFac;
