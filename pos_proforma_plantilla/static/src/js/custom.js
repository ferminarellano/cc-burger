odoo.define('pos_proforma_plantilla.change_bill_template', function(require){
    "use strict";
	
	var model = require('pos_restaurant.printbill');
	
	var core = require('web.core');
	var QWeb = core.qweb;

	model.BillScreenWidget.prototype.render_receipt = function(){
		var order = this.pos.get_order();
		var receipt = order.export_for_printing();
		receipt.bill = true;
		
        this.$('.pos-receipt-container').html(QWeb.render('BillReceipt',{
				receipt: receipt,
                widget: this,
				pos: this.pos,
                order: order,
            }));
			
        this.$('.receipt-paymentlines').remove();
        this.$('.receipt-change').remove();
	};

});

