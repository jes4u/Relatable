// basically still need to figure out how to store current url.
// ---------
chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
   function(tabs){
      letsgetthisbread(tabs[0].url);
   }
);


function myFunction(tablink) {
  // do stuff here
  console.log(tablink);
}

var currentBody = document.getElementsByTagName("BODY")[0];
console.log(currentBody);

var letsgetthisbread = async (url2) => {
//    const url = "http:/206.87.108.98:5000/query/?url=https://hackernoon.com/top-python-web-development-frameworks-to-learn-in-2019-21c646a09a9a";
    const url = "http:/206.87.108.98:5000/query/?url=" + url2;
    let request = new Request(url, {
        method: "GET",
        headers: new Headers()
    });
    this.callBackend(request)
        .then(res => {
            console.log(res)

            var cards = document.getElementsByClassName("card-body");
            for ( var i = 0 ; i < cards.length ; i++) {
                cards[i].innerHTML = "<a href="+res.pages[i]+" target='_blank'>" + res.titles[i] + "</a>";
            }
            var afterLoad = document.getElementsByClassName("afterLoad");
            for ( var i = 0 ; i < afterLoad.length ; i++) {
                afterLoad[i].classList.remove("afterLoad");
            }
            var beforeLoad = document.getElementsByClassName("beforeLoad");
            for ( var i = 0 ; i < beforeLoad.length ; i++) {
                beforeLoad[i].classList.add("toggleOff");
            }
        })
        .catch(err => console.log(err));
};

callBackend = async request => {
    const response = await fetch(request);
    const body = await response.json();
    if (response.status !== 200) {
        console.log(response.status)
        throw Error(body.message);
    }
    return body;
}


window.onload = function() {
    letsgetthisbread();
}

