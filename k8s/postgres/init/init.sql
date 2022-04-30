create table word (
	word varchar primary key
);

create table daily_word (
	date date primary key,
	word varchar not null,
	foreign key (word) references word(word)
)