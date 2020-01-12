// basically still need to figure out how to store current url.
// ---------
chrome.tabs.getSelected(null, function(tab) {
    myFunction(tab.url);
});

function myFunction(tablink) {
  // do stuff here
  console.log(tablink);
}
// ---------

var letsgetthisbread = async () => {
    const url = "http:/206.87.108.98:5000/query/?url=https://hackernoon.com/top-python-web-development-frameworks-to-learn-in-2019-21c646a09a9a";
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
//            var json = res.body;
//            document.getElementById('test').innerHTML = json;
//            var links_output = document.getElementById("links");
//            links_output.innerHTML = '';
//            for (var key of json) {
//                links_output.innerHTML = links_output.innerHTML + '<div><h3>' + key + '</h3><br>';
//                for (var links of json[key]) {
//                    links_output.innerHTML = links_output.innerHTML + '<a href="' + '">' + json[key][links] + '</a></div><br>';
//                }
//            }
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

