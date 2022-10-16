
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
    const urlly = new URL("http://10.49.7.146:5000/query");
    const contents = {
    contentType: "text/plain"
  }

    const rawResponse = fetch(urlly, {
      method: 'POST',
      headers: contents,
      body: request.source
      }).then((res) => res.json()).then((data) =>  doStuff(data))
      
    }

      // alert(rawResponse);
  });

function doStuff(data){
  console.log(data)
  

  document.getElementById("co2ScoreLine").setAttribute('value', data["total_carbon"]);
  document.getElementById("carbon-score").innerText = data["total_carbon"] + " Kg of CO2"
  document.getElementById("waterScoreLine").setAttribute('value', data["total_water"]);
  document.getElementById("water-score").innerText = data["total_water"] + " Liters of water"
  
  // alert(JSON.stringify(data));

  const ingredientsKeys = Object.keys(data.scores);
  var ingredients = []
  for (let ing in data.scores){
    ingredients.push(data.scores[ing]);
  } 
  
  // var sortCarbon = ingredients.slice().sort(function(a,b){return a.carbonScore-b.carbonScore});

  // message.innerText = ingredients;
  // message.innerText = text;


  for (let i = 0; i < ingredientsKeys.length && i < 2; i++){
    document.getElementById(i+1+"-co2-worst").innerText = ingredientsKeys[i];
    document.getElementById(i+1+"-water-worst").innerText = ingredientsKeys[i];
  }
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


// Then use it like so with async/await:
