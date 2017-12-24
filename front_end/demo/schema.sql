drop table if exists bonds;
create table bonds(
	id integer primary key autoincrement,
	coupon_rate float not null,
	face_value float not null,
	time_start date not null,
	year float not null,
	time_cur date not null,
	frequency float not null,
);
