SELECT t1.order_id, t1.customer_id, t1.employee_id, t1.order_date, t1.required_date, 
t1.shipped_date, t1.ship_via, t1.freight, t1.ship_name, t1.ship_address, 
t1.ship_city, t1.ship_region, t1.ship_postal_code, t1.ship_country, t2.product_id, 
t2.unit_price, t2.quantity, t2.discount, t3.product_name, t3.supplier_id, 
t3.category_id, t3.quantity_per_unit, t3.unit_price, t3.units_in_stock, 
t3.units_on_order, t3.reorder_level, t3.discontinued, t4.last_name, t4.first_name, 
t4.title, t4.title_of_courtesy, t4.birth_date, t4.hire_date, t4.address, t4.city, 
t4.region, t4.postal_code, t4.country, t4.home_phone, t4.extension, t4.photo, 
t4.notes, t4.reports_to, t4.photo_path, t5.shipper_id, t5.company_name, t5.phone, 
t6.company_name, t6.contact_name, t6.contact_title, t6.address, t6.city, t6.region, 
t6.postal_code, t6.country, t6.phone, t6.fax, t7.company_name, t7.contact_name, 
t7.contact_title, t7.address, t7.city, t7.region, t7.postal_code, t7.country, 
t7.phone, t7.fax, t7.homepage
	FROM public.orders AS t1, public.order_details AS t2, public.products t3,
	     public.employees AS t4, public.shippers AS t5, public.customers t6,
		 public.suppliers AS t7
	WHERE t1.order_id = t2.order_id AND
	      t2.product_id = t3.product_id AND
		  t1.employee_id = t4.employee_id AND
		  t1.ship_via = t5.shipper_id AND
		  t1.customer_id = t6.customer_id AND
		  t3.supplier_id = t7.supplier_id;