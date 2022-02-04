var csrftoken = Cookies.get('csrftoken');

function excluir_categoria(pk) {
    if (confirm('Deseja realmente excluir esta categoria?')) {
        $.ajax({
            type: 'post',
            url: '/excluir_categoria/' + pk,
            data: { csrfmiddlewaretoken: csrftoken, },
            dataType: 'json',
            success: function (response) {
                $('#categoria_' + pk).remove();
            },
        });
    }
}