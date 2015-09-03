App = Ember.Application.create();

App.Router.map(function() {
    //Crea controller y vista para proveedores
    this.resource('proveedores', function(){
          this.route('descripcion', {path:'/:proveedor_id/descripcion'});
    });
});

App.ProveedoresRoute = Ember.Route.extend({
   model: function(){
       return [
               {index:1, nombre:'Proveedor1'},
               {index:2, nombre:'Proveedor2'},
               {index:3, nombre:'Proveedor3'}
              ]
   }
});

App.ProveedoresDescripcionRoute = Ember.Route.extend({
    model: function(params) {
          return Ember.$.getJSON('http://localhost:8000/api/proveedores').then(function(data){
             return data.findBy('id', parseInt(params.proveedor_id));
          });
    }
});

App.IndexRoute = Ember.Route.extend({
   model: function() {
       return $.getJSON('http://localhost:8000/api/productos');
   }
});


App.IndexController = Ember.Controller.extend({
     actions: {
         actualizarInventario: function(){
             var productoElegido = $("#txt-compra").val(),
                 cantidadElegida = $("#txt-cantidad").val(),
                 productoRestante = 0,
                 id  = 0;

             $('tr').each(function(){
                    var producto = $(this).children('td:first-of-type').html();
                    if(productoElegido.trim() === producto.trim()){
                        id =  $(this).attr('id');
                        productoRestante =  parseInt($(this).children('td:last-of-type').html()) - parseInt(cantidadElegida);
                    }
             });

             $.ajax({
                         beforeSend: function(request){
                            request.setRequestHeader('X-CSRFToken', getCookie("csrftoken"));
                            request.setRequestHeader('X-HTTP-Method-Override', 'PUT');
                         },
                         url:"http://localhost:8000/api/productos/"+ id+"/",
                         contentType: 'application/json',
                         dataType: 'json',
                         type: 'post',
                         data:JSON.stringify({
                             'id': parseInt(id),
                             'nombre': productoElegido,
                             'cantidad':productoRestante
                         })

             }).done(function() {
                    alert("Compra realizada, el inventario ha sido actualizado");
                });
         }
     }
});

