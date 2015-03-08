openerp.ui_translation = function(instance){

    var QWeb = instance.web.qweb,
    _t = instance.web._t;

    instance.ui_translation = {};

    instance.web.ViewManager.include({
        start: function() {
            this.$el.mousedown(this, this.translate_view);
            $(document.body).mousedown(this, this.translate_body);
            this._super();
        },

        translate_view: function(event){
            if(!event.ctrlKey){ return;}
            event.stopPropagation();
            event.preventDefault();
            event.data.translate_terms(event.srcElement,
                                       event.data.dataset.model)
        },

        translate_body: function(event){
            if(!event.ctrlKey){ return;}
            event.stopPropagation();
            event.preventDefault();
            event.data.translate_terms(event.srcElement)
        },

        translate_terms: function(srcElement, current_model){
            console.log(srcElement.textContent.trim());
            var self = this;
            this.session.rpc(
                "/web/ui_translation/get_translate_wizard",
                {label: srcElement.textContent.trim(),
                 model: current_model}
            ).then(
                function(result) {
                    if (!result.is_action){
                        return self.do_warn(_("Can't translate this string"),
                                            result.value);
                    } else {
                        return self.do_action(result.value, {
                            on_close: function(){
                                // It could be great to get result from
                                // Translate action to avoir to reload the
                                // entire page
                                location.reload();
                            }
                        });
                    }
                }
            );
        },
    });
};
