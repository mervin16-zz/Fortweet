$(document).ready(function(){
    
    // Socket connection to server
    var socket = io.connect('http://127.0.0.1:5000')

    // Listens for tweets
    socket.on('stream-results', function(results){

      // Insert tweets in divs
      $('#live-tweet-container').prepend(`
      <div class="row justify-content-md-center mt-3">
        <div class="col-md-2">
            <img width="56px" height="56px"  src="${results.profile_pic !== "" ? results.profile_pic : "/static/icons/profile-pic.png"}" class="mx-auto d-block rounded"  alt="">
        </div>
        <div class="col-md-8 my-auto">
          <div><b>${results.author}</b></div>
          <div>${results.message}</div>
        </div>
      </div>
      `);
    });

    // Listener for when a stream of tweets starts
    socket.on('stream-started', function(bool){
      if(bool==true){
        $("#favicon").attr("href","/static/icons/fortnite-active.png");
        $("#stream-status-ic").attr("src","/static/icons/stream-active.png");
        $("#stream-status-text").text("Live stream active");
      }
    });

    // Listener for when a stream of tweets ends
    socket.on('stream-ended', function(bool){
      if(bool==true){
        $("#favicon").attr("href","/static/icons/fortnite-inactive.png");
        $("#stream-status-ic").attr("src","/static/icons/stream-inactive.png");
        $("#stream-status-text").text("Live stream inactive");
      }
    });

  });