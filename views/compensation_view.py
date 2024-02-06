<odoo>
  <data>

    <record id="view_order_form_inherit_to_check" model="ir.vi.view">
      <field name="name">sale.order.form.to.check</field>
      <field name="model">sale.order</name>
      <field name="inherit_id" ref="sale.view_order_form"/>
      <field name="arch" type="xml">
        <field name="payment_term_id" position="after">
          <field name="to_check"/>
        </field>
      </field>
    </record>

  </data>
</odoo>