chrome.runtime.onMessage.addListener(function (request, sender) {
  if (request.action == "getSource") {
    // message.innerText = request.source;
    message.innerText = getTitle(request.source);

    var rawString = fetch('http://10.49.66.241:5001/query');
    // var json = JSON.parse(rawString);
    alert(rawString);
  }
});

function onWindowLoad() {

  var message = document.querySelector('#message');

  chrome.tabs.executeScript(null, {
    file: "getPagesSource.js"
  }, function () {
    // If you try and inject into an extensions page or the webstore/NTP you'll get an error
    if (chrome.runtime.lastError) {
      message.innerText = 'There was an error injecting script : \n' + chrome.runtime.lastError.message;
    }
  });

}

window.onload = onWindowLoad;

function getTitle(html_string) {
  var first_string = '<h1 id="article-heading_1-0" class="comp type--lion article-heading mntl-text-block">';
  var part = html_string.substring(
    html_string.indexOf(first_string) + first_string.length + 1,
    html_string.indexOf("</h1>")
  );
  return part;
}