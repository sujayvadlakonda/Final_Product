$(document).ready(function(){
    let clothingData, schoolData;

    $.ajax({
        url:'http://localhost:5990'
    }).error(function(error){
        console.log('error', error)
    }).success(function(data){
        clothingData = data
        setSchoolData('frisco')
    });

    function setSchoolData (schoolKey) { 
        schoolData = clothingData[schoolKey]
    };

    function loadSchool (schoolKey) {
        setSchoolData(schoolKey)
        loadCategory('tShirt')
    }

    function loadCategory (category){
        $('.main-content').empty()
        schoolData[category].foreach(item => {
            $('.main-content').append(`
                <div class="card col-sm-12 col-md-6 col-lg-4 col-xl-3" style="width: 18rem;">
                    <img src="${item.img_src}" class="card-img-top">
                    <div class="card-body">
                <h5 class="card-title"> ${item.title}</h5>
                <p class="card-text"> ${item.price} </p>
                <a href="${ item.url }" class="btn btn-primary" target="_blank">View Product</a>
            </div>
        </div>
            `)
        });
    }

    $('school-dropdown').select(function(){
        loadSchool($(this).attr('id'))
    })

})

