$('.category').click(function(){
    let category_id = $(this).attr('category_id')
    let url = '/api/v1/portfillo/get_by_categoty/' + category_id + "/?format=html"
    try {
        $.get(url, function (data){
            let portfile_element = $('#portfillo_section')
            portfile_element.empty();
            portfile_element.append(data)
        })
    } catch (error) {
        alert('Error')
    }
})