$(document).ready(function () {

  /************************************/
  /*********** My Functions ***********/
  /************************************/
  function stream_active_setup() {
    $("#favicon").attr("href", "/static/icons/fortnite-active.png");
    $("#stream-status-ic").attr("src", "/static/icons/stream-active.png");
    $("#stream-status-text").text("Live stream active");
  }

  function stream_inactive_setup() {
    $("#favicon").attr("href", "/static/icons/fortnite-inactive.png");
    $("#stream-status-ic").attr("src", "/static/icons/stream-inactive.png");
    $("#stream-status-text").text("Live stream inactive");
  }



  /*********************************/
  /*********** My Events ***********/
  /*********************************/

  // Socket connection to server

  // Prometheus
  //var socket = io.connect('http://104.131.173.145:8083');

  // Local
  var socket = io().connect(window.location.protocol + '//' + document.domain + ':' + location.port, {
    transports: ['websocket']
  });

  // Heroku
  //var socket = io.connect('https://fortweet.herokuapp.com/');

  // Send a hello to know
  // if a stream is already active
  socket.on('connect', () => {
    socket.emit('hello-stream', 'hello-stream');
  });

  // Listene for reply from hello
  socket.on('hello-reply', function (bool) {
    if (bool == true) {
      stream_active_setup()
    } else {
      stream_inactive_setup()
    }
  });

  // Listens for tweets
  socket.on('stream-results', function (results) {

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
  socket.on('stream-started', function (bool) {
    if (bool == true) {
      stream_active_setup()
    }
  });

  // Listener for when a stream of tweets ends
  socket.on('stream-ended', function (bool) {
    if (bool == true) {
      stream_inactive_setup()
    }
  });

});