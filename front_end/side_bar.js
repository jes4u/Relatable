var letsgetthisbread = async () => {
    const url = "http:/206.87.108.98:5000/query";
    let request = new Request(url, {
        method: "GET",
        headers: new Headers()
    });
    this.callBackend(request)
        .then(res => {
            var json = res.body;
            document.getElementById('test').innerHTML = json;
            var links_output = document.getElementById("links");
            links_output.innerHTML = '';
            for (var key of json) {
                links_output.innerHTML = links_output.innerHTML + '<div><h3>' + key + '</h3><br>';
                for (var links of json[key]) {
                    links_output.innerHTML = links_output.innerHTML + '<a href="' + '">' + json[key][links] + '</a></div><br>';
                }
            }
        })
        .catch(err => console.log(err));
};

callBackend = async request => {
    const response = await fetch(request);
    const body = await response.json();
    if (Response.status !== 200) {
        throw Error(body.message);
    }
    return body;
}


window.onload = function() {
    letsgetthisbread();
}

