var letsgetthisbread = function() {
    return new Promise(function(resolve, reject) {
        var post = new XMLHttpRequest();
        
        //change this
        var url_get = "10.19.133.160:5000/query/?url=https://hackernoon.com/top-python-web-development-frameworks-to-learn-in-2019-21c646a09a9a";
        
        post.open("GET", url_get, true);

        //possibly change this
        post.setRequestHeader('Content-Type', 'application/json');
        //post.send(document.body.innerHTML);
        if (post.status == 200) {
            
            var json = response.body;
            document.getElementById('test').innerHTML = (json);
            var links_output = document.getElementById("links");
            links_output.innerHTML = '';
            for (var key of json) {
                links_output.innerHTML = links_output.innerHTML + '<div><h3>' + key + '</h3><br>';
                for (var links of json[key]) {
                    links_output.innerHTML = links_output.innerHTML + '<a href="' + '">' + json[key][links] + '</a></div><br>';
                }
            }
            resolve();
      } else {
            reject();
      }
    });
  }

window.onload = function() {
    letsgetthisbread()
}

