searchElea = function(word){
    var query = word.selectionText;
    var url = "https://www.ebay.com/sh/research?dayRange=365&sorting=-avgsalesprice&tabName=SOLD&keywords="
    + query;
    window.open("C:\Users\avery\Desktop\CS2112Java\Elea\popup.html", 'popUpWindow','height=500,width=500',false);
};


chrome.contextMenus.removeAll(function() {
    chrome.contextMenus.create({
     id: "1",
     title: "Elea this!",
     contexts:["selection"],  // ContextType
    }); })

chrome.contextMenus.onClicked.addListener(searchElea);