$(document).ready(function () {
    // eel.init()();  // Commented if not needed

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },
    });
});
