chrome.tabs.executeScript({
  code: "window.getSelection().toString();"
}, function (selection) {
  document.getElementById('demo').innerHTML = selection[0];
});
