(function() {

    var width = 320;    // We will scale the photo width to this
    var height = 0;     // This will be computed based on the input stream
    var streaming = false;
    var video = null;
    var canvas = null;
    var photo = null;
    let btn_capture = document.getElementById('capture')
    let btn_recapture = document.getElementById('recapture')
    let btn_div = document.getElementById('exam2-btn')

    function startup() {   // 기본 사진 촬영 함수
    console.log("startup")
      video = document.getElementById('video');
      canvas = document.getElementById('canvas');
      photo = document.getElementById('photo');

      navigator.mediaDevices.getUserMedia({video: true, audio: false})
      .then(function(stream) {
        video.srcObject = stream;
        video.play();
      })
      .catch(function(err) {
        console.log("An error occurred: " + err);
      });

      video.addEventListener('canplay', function(ev){
        if (!streaming) {
          height = video.videoHeight / (video.videoWidth/width);

          // Firefox currently has a bug where the height can't be read from
          // the video, so we will make assumptions if this happens.

          if (isNaN(height)) {
            height = width / (4/3);
          }

          video.setAttribute('width', width);
          video.setAttribute('height', height);
          canvas.setAttribute('width', width);
          canvas.setAttribute('height', height);
          streaming = true;
        }
      }, false);

      setTimeout(function(){  // 캡쳐 시간
        takepicture()
    }, 4000);
    }

    function restartup() {   // 재촬영 함수
      console.log("restartup")
        video = document.getElementById('video');
        canvas = document.getElementById('canvas');
        photo = document.getElementById('photo');

        video.style.display = 'flex'
        photo.style.display = 'none'

        navigator.mediaDevices.getUserMedia({video: true, audio: false})
        .then(function(stream) {
          video.srcObject = stream;
          video.play();
        })
        .catch(function(err) {
          console.log("An error occurred: " + err);
        });
  
        video.addEventListener('canplay', function(ev){
          if (!streaming) {
            height = video.videoHeight / (video.videoWidth/width);
  
            // Firefox currently has a bug where the height can't be read from
            // the video, so we will make assumptions if this happens.
  
            if (isNaN(height)) {
              height = width / (4/3);
            }
  
            video.setAttribute('width', width);
            video.setAttribute('height', height);
            canvas.setAttribute('width', width);
            canvas.setAttribute('height', height);
            streaming = true;
          }
        }, false);
  
        setTimeout(function(){  // 캡쳐 시간
          retakepicture()
      }, 4000);
  
  //      clearphoto();
        
      }

    // Fill the photo with an indication that none has been
    // captured.

    function clearphoto() {
      var context = canvas.getContext('2d');
      context.fillStyle = "#AAA";
      context.fillRect(0, 0, canvas.width, canvas.height);

      var data = canvas.toDataURL('image/png');
      photo.setAttribute('src', data);
    }
    function reclearphoto() {
      var context = canvas.getContext('2d');
      context.fillStyle = "#AAA";
      context.fillRect(0, 0, canvas.width, canvas.height);

      var data = canvas.toDataURL('image/png');
      photo.setAttribute('src', data);
   
    }

    // Capture a photo by fetching the current contents of the video
    // and drawing it into a canvas, then converting that to a PNG
    // format data URL. By drawing it on an offscreen canvas and then
    // drawing that to the screen, we can change its size and/or apply
    // other changes before drawing it.

    function takepicture() {
      var context = canvas.getContext('2d');
      if (width && height) {
        canvas.width = width;
        canvas.height = height;
        context.drawImage(video, 0, 0, width, height);

        var data = canvas.toDataURL('image/png');
   
//        alert("here"+canvas.toDataURL())
        photo.setAttribute('src', data);
        video.style.display = 'none'  // 비디오 안보이기
        btn_recapture.style.display = 'inline-block'
        btn_div.style.marginTop = '20px'
      } else {
        clearphoto();
      }
    }

    function retakepicture() {
      var context = canvas.getContext('2d');
      if (width && height) {
        canvas.width = width;
        canvas.height = height;
        context.drawImage(video, 0, 0, width, height);

        var data = canvas.toDataURL('image/png');
   
//        alert("here"+canvas.toDataURL())
        photo.setAttribute('src', data);
        photo.style.display = 'inline-block'
        video.style.display = 'none'  // 비디오 안보이기
      } else {
        reclearphoto();
      }
    }

    // Set up our event listener to run the startup process
    // once loading is complete.
    window.addEventListener('load',startup)
    btn_recapture.addEventListener('click', restartup, false);
  })();