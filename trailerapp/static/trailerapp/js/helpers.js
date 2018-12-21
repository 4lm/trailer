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
