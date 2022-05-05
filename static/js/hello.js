$.getJSON("/users",
        function(data) {
          $('body').append('<div>users:</div>')
          for (var i = 0; i < data.length; i++){
            $('body').append('<div>'+data[i].name+'</div>')
          }
        });
