var csrftoken = Cookies.get('csrftoken');

function excluir_produto(pk) {
    if (confirm('Deseja realmente excluir este produto?')) {
        $.ajax({
            type: 'post',
            url: '/excluir_produto/' + pk,
            data: { csrfmiddlewaretoken: csrftoken, },
            dataType: 'json',
            success: function (response) {
                $('#produto_' + pk).remove();
            },
        });
    }
}