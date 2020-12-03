
    $(document).ready(function(){
      // Socket connection to server
      var socket = io.connect('http://127.0.0.1:5000');
      var is_streaming = false;

      $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
      });

      $("#tweets-live-start").click(function(){
        if (is_streaming == true){
          alert("A stream is already running")
        }else{
          $.ajax({
            type: "POST",
            url : "/admin/startstream",
            data: {url : "print \"hello\""},
            contentType: 'application/json;charset=UTF-8'
          });
        }
      });

      // Listener for when a stream of tweets starts
      socket.on('stream-started', function(bool){
        if(bool==true){
          // Set the flag
          is_streaming = true

          // Style components
          $("#stream-status-ic").attr("src","/static/icons/stream-active.png");
          $("#tweets-live-start").removeClass("ftweet-text-starttweets-inactive").addClass("ftweet-text-starttweets-active")
          $("#tweets-live-start span").text("Streaming");
        }
      });

      // Listener for when a stream of tweets ends
      socket.on('stream-ended', function(bool){
        if(bool==true){
          // Set the flag
          is_streaming = false

          // Style components
          $("#stream-status-ic").attr("src","/static/icons/stream-inactive.png");
          $("#tweets-live-start").removeClass("ftweet-text-starttweets-active").addClass("ftweet-text-starttweets-inactive")
          $("#tweets-live-start span").text("Start Stream");
        }
      });
    });