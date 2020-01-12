chrome.runtime.onMessage.addListener(function(msg, sender){
    if(msg == "toggle"){
        toggle();
    }
})

var iFrame = document.createElement('iframe');
iFrame.style.background = "green";
iFrame.style.height = "100%";
iFrame.style.width = "0px";
iFrame.style.position = "fixed";
iFrame.style.top = "0px";
iFrame.style.right = "0px";
iFrame.style.zIndex = "9000000000000000000";
iFrame.frameBorder = "none";
iFrame.src = chrome.extension.getURL("popup.html")

document.body.appendChild(iframe);

function toggle(){
    if(iframe.style.width == "0px"){
        iframe.style.width="400px";
    }
    else{
        iframe.style.width="0px";
    }
}