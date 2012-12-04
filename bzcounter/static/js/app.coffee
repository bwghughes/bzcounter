class Tipple
    constructor: (id, name, units) ->
        @id = id
        @name = name
        @units = units


class TippleViewModel
    constructor:  ->
        @createdAt = Date.now()
        @tipples = ko.observableArray([
            new Tipple('PP', "Pint of Pedi", 3.6),
            new Tipple('LW', "Large Wine", 3.0),
            new Tipple('GT', "Gin and Tonic", 2),
        ])

    registerClick: (id) =>
        tipple = @tipples().filter (tipple) -> tipple.id == id
        if not tipple[0].count
            tipple[0].count = 0
        tipple[0].count++


$ ->
    window.tvm = new TippleViewModel()
    ko.applyBindings(window.tvm);

    $('.add').tap ->
        window.tvm.registerClick(this.id)

    $('#done').tap ->
        $.ajax '/i/',
            type: 'POST',
            contentType: 'application/json',
            dataType: 'json',
            data: ko.toJSON(window.tvm),
            success: (data) ->
                alert 'Thanks for being so honest.'




