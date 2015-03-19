openerp.testing.section('UI Translation tests',
                        {
                            dependencies: ['web.ViewManager', 'ui_translation'],
                            setup: function(instance){
                                //do things before each test
                            },
                            teardown: function(instance){
                                //do things after each test
                            }
                        }, function (test) {

    test('Hello ui_translation', function (instance) {
        var ui_trans = new instance.ui_translation.SomeType("Pierre");
        strictEqual(ui_trans.display_value(),
                    "Value is Pierre", "Test object function, param should be " +
                                       "set in constructor");
        ok(instance.ui_translation.true_value, "Test static variable");
        strictEqual(instance.ui_translation.static_method('Dam'),
                    "Hello Dam!", "Test static method");
    });


    test('Hello viewManager', function (instance) {
        var vm = new instance.web.ViewManager();
        strictEqual(vm.say_hello('Pierre'),
                    "Hello Pierre!", "should have provided value in constructor");
    });

    test('Translate terms with mock', {rpc: 'mock', asserts: 2},
         function(instance, $el, mock){

        var wizard_mock = false;

        mock('/web/ui_translation/get_translate_wizard', function(context){
            deepEqual(context.params, {label: "Hello the world", model: 'model.test'},
                      "context sent to the server");
            wizard_mock = true;
            return {value: "mock result",
                    is_action: false};
        });
        $el.html('<span> Hello the world 	 </span>');
        var vm = new instance.web.ViewManager();
        return vm.translate_terms($el.find("span")[0], 'model.test').then(function (result) {
            ok(wizard_mock, 'mock service was called');
        });
    });
});

