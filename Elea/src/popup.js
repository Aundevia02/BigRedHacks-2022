async function fetchInfo(urlly){
  
 const post = await fetch(urlly, { // URL as http://www.example.com/?foo=bar&fizz=buzz
    method: "POST",
    headers: contents,
    body: request.source // The actual body
  });

  message.innerText = post;
  alert(post);
}



chrome.runtime.onMessage.addListener(function (request, sender) {
  if (request.action == "getSource") {
    // message.innerText = request.source;
    message.innerText = getTitle(request.source);
    
    // const data = {
    //   ingredients: request.source
    // }
    
    // const post = await fetchInfo(urlly);
    
    // var json = JSON.parse(rawString);
    // alert(post);

    // var json = JSON.parse(post)
    const urlly = new URL("http://10.49.66.241:5001/query");
    const contents = {
    contentType: "text/plain"
  }

    const rawResponse = fetch(urlly, {
      method: 'POST',
      headers: contents,
      body: request.source
      }).then((res) => res.json()).then((data) =>  doStuff(data)
      )
      
    }

      // alert(rawResponse);
  });

function doStuff(data){
  console.log(data)
  
  message.innerText = data["scores"];
}

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

async function getInfo(){
  const urlly = new URL("http://10.49.66.241:5001/query");
  const contents = {
    contentType: "text/plain"
  }
  getDevices = async () => {
    const settings = {
        method: 'POST',
        headers: contents,
        body : request.source
    };
    try {
      const fetchResponse = await fetch(url, settings);
      const data = await fetchResponse.json();
      message.innerText = data;
  } catch (e) {
      alert(e);
  }
  }

  // message.innerText = getDevices;
}

// Then use it like so with async/await:
