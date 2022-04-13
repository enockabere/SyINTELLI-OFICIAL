$(document).ready(function () {
    $("#accs").click(function () {
        $("#accs").css("background", "transparent")
    })
    $("#quoteBtn").click(function () {
        $(".myForm").toggle(500);
        $("#quoteBtn").hide();
    })

})
//Get the button:
mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
    } else {
        mybutton.style.display = "none";
    }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
// window.
// onload
//     = function () {
//         Particles.
//         init
//             ({
//                 selector: '.background',
//                 preset: "Confettis",
//                 maxParticles: 450,
//                 connectParticles: false,
//                 color: '#600606',
//                 speed: 1,
//                 sizeVariations: 5,
//             });
//     };

window.addEventListener('DOMContentLoaded', (event) => {
    /* ---- particles.js config ---- */

    particlesJS("particles", {

        "particles": {
            "number": {
                "value": 12,
                "density": {
                    "enable": true,
                    "value_area": 100
                }
            },
            "color": {
                "value": "#600606"
            },
            "shape": {
                "type": "polygon",
                "stroke": {
                    "width": 1,
                    "color": "#fff"
                },
                "polygon": {
                    "nb_sides": 6
                },

            },
            "opacity": {
                "value": 0.10422178395625899,
                "random": true,
                "anim": {
                    "enable": false,
                    "speed": 1,
                    "opacity_min": 0.1,
                    "sync": false
                }
            },
            "size": {
                "value": 5.2388442605866,
                "random": true,
                "anim": {
                    "enable": true,
                    "speed": 0,
                    "size_min": 100,
                    "sync": true
                }
            },
            "line_linked": {
                "enable": true,
                "distance": 352.750653390415,
                "color": "#ffffff",
                "opacity": 0.5211089197812949,
                "width": 4.810236182596569
            },
            "move": {
                "enable": true,
                "speed": 3.206824121731046,
                "direction": "none",
                "random": true,
                "straight": false,
                "out_mode": "out",
                "bounce": false,
                "attract": {
                    "enable": true,
                    "rotateX": 600,
                    "rotateY": 1200
                }
            }
        },
        "interactivity": {
            "detect_on": "window",
            "events": {
                "onhover": {
                    "enable": false,
                    "mode": "repulse"
                },
                "onclick": {
                    "enable": false,
                    "mode": "repulse"
                },
                "resize": true
            },
            "modes": {
                "grab": {
                    "distance": 400,
                    "line_linked": {
                        "opacity": 1
                    }
                },
                "bubble": {
                    "distance": 400,
                    "size": 40,
                    "duration": 2,
                    "opacity": 8,
                    "speed": 3
                },
                "repulse": {
                    "distance": 200,
                    "duration": 0.4,
                    "line_linked": {
                        "opacity": 1
                    }
                },
                "push": {
                    "particles_nb": 4
                },
                "remove": {
                    "particles_nb": 2,
                }

            }
        },
        "retina_detect": true,

    });
});