const api = location.origin;

async function callPow() {
  const base = +document.getElementById('pow-base').value;
  const exponent = +document.getElementById('pow-exp').value;
  const output = document.getElementById('pow-res');

  try {
    const res = await fetch(api + '/math/pow', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ base, exponent }),
    });
    const data = await res.json();

    if (!res.ok) {
      // FastAPI may return detail as string or array of { msg, ... }
      let msg = '';
      if (Array.isArray(data.detail)) {
        msg = data.detail.map(e => e.msg).join('; ');
      } else {
        msg = data.detail || `HTTP ${res.status}`;
      }
      output.textContent = 'Error: ' + msg;
    } else {
      output.textContent = 'Result: ' + data.result;
    }
  } catch (err) {
    output.textContent = 'Error: ' + err.message;
  }
}

async function callFib() {
  const n = +document.getElementById('fib-n').value;
  const output = document.getElementById('fib-res');

  try {
    const res = await fetch(`${api}/math/fib/${n}`);
    const data = await res.json();

    if (!res.ok) {
      let msg = '';
      if (Array.isArray(data.detail)) {
        msg = data.detail.map(e => e.msg).join('; ');
      } else {
        msg = data.detail || `HTTP ${res.status}`;
      }
      output.textContent = 'Error: ' + msg;
    } else {
      output.textContent = 'Result: ' + data.result;
    }
  } catch (err) {
    output.textContent = 'Error: ' + err.message;
  }
}

async function callFac() {
  const n = +document.getElementById('fac-n').value;
  const output = document.getElementById('fac-res');

  try {
    const res = await fetch(`${api}/math/fact/${n}`);
    const data = await res.json();

    if (!res.ok) {
      let msg = '';
      if (Array.isArray(data.detail)) {
        msg = data.detail.map(e => e.msg).join('; ');
      } else {
        msg = data.detail || `HTTP ${res.status}`;
      }
      output.textContent = 'Error: ' + msg;
    } else {
      output.textContent = 'Result: ' + data.result;
    }
  } catch (err) {
    output.textContent = 'Error: ' + err.message;
  }
}

// Attach to window so your buttons still work:
window.callPow = callPow;
window.callFib = callFib;
window.callFac = callFac;
