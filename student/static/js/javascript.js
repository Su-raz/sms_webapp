$(document).ready(function() {
    var table = $('#example').DataTable( {
        lengthChange: false,
 
        buttons: [ { extend:'print',
        text: 'Print List' ,
        title: 'Student List',

        customize:function ( win ) {
                        $(win.document.body).find('h1').css('text-align', 'center');
                        $(win.document.body).css( 'font-size', '10px' );
                        $(win.document.body).css( 'text-align', 'center' );
                        // $(win.document.body).find( 'table' )
                        // .addClass( 'compact' )
                        // .css( 'font-size', 'inherit' );
                }

        	}],

        scrollY: 300,
        scrollX: true,

    } );
 
    table.buttons().container()
        .appendTo( '#example_wrapper .col-md-6:eq(0)' );
} );




$(document).ready(function() {
    var table = $('#example1').DataTable( {
        lengthChange: false,


        scrollY: 300,
        scrollX: true,

    } );
 
    // table.buttons().container()
    //     .appendTo( '#example_wrapper .col-md-6:eq(0)' );
} );


