// Play only one video at the time
// https://stackoverflow.com/questions/33382696/
// videojs-when-playing-video-pausing-all-other-videos
$(".video-js").each(function (videoIndex) {

    var videoId = $(this).attr("id");

    videojs(videoId).ready(function () {
        this.on("play", function (e) {
            //pause other video
            $(".video-js").each(function (index) {
                if (videoIndex !== index) {
                    this.player.pause();
                }
            });
        });

    });
});


// Stop playing if not in viewport
// https://stackoverflow.com/questions/21163756/
// html5-and-javascript-to-play-videos-only-when-visible
$(window).scroll(function () {
    $(".video-js").each(function () {
        if (($(this).is(":in-viewport")) === false) {
            this.player.pause();
        }
    })
});


// Remove cookie notice after accepting it
$(document).ready(function () {
   $('.close-cookies').click(function () {
       $(this).parent().hide();
   });
});