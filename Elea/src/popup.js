chrome.tabs.executeScript({
  code: "window.getSelection().toString();"
}, function (selection) {
  document.getElementById('ingredients').innerHTML = selection[0];
});
