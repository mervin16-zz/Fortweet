
    $(document).ready(function(){

      /************************************/
      /*********** My Functions ***********/
      /************************************/
      function stream_active_setup(){
          // Set the flag
          is_streaming = true

          // Style components
          $("#stream-status-ic").attr("src","/static/icons/stream-active.png");
          $("#tweets-live-start").removeClass("ftweet-text-starttweets-inactive").addClass("ftweet-text-starttweets-active")
          $("#tweets-live-start span").text("Streaming");
      }

      function stream_inactive_setup(){
        // Set the flag
        is_streaming = false

        // Style components
        $("#stream-status-ic").attr("src","/static/icons/stream-inactive.png");
        $("#tweets-live-start").removeClass("ftweet-text-starttweets-active").addClass("ftweet-text-starttweets-inactive")
        $("#tweets-live-start span").text("Start Stream");
      }


      /*********************************/
      /*********** My Events ***********/
      /*********************************/
      
      // Socket connection to server
      //var socket = io.connect('http://104.131.173.145:8083');
      var socket = io.connect('http://localhost:8083');
      var is_streaming = false;

      // Send a hello to know
      // if a stream is already active
      socket.on('connect', () => {    
        socket.emit('hello-stream', 'hello-stream');
      });
  
      // Listene for reply from hello
      socket.on('hello-reply', function(bool){
        if(bool==true){
          stream_active_setup()
        }else{
          stream_inactive_setup()
        }
      });

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
          stream_active_setup()
        }
      });

      // Listener for when a stream of tweets ends
      socket.on('stream-ended', function(bool){
        if(bool==true){
          stream_inactive_setup()
        }
      });
    });