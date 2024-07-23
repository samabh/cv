$('#multi_slider').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:6
        },
        600:{
            items:6
        },
        1000:{
            items:6
        }
    },
    dots:true,
    autoplay:true,
})

function toggleAnswer(answerId) {
    var answerRow = document.getElementById('answer' + answerId);
    if (answerRow.style.display === 'table-row') {
        answerRow.style.display = 'none';
    } else {
        answerRow.style.display = 'table-row';
    }
}
