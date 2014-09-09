%importdata(shares_csv.csv)
clear; clc
bm=importdata('/srv/vhosts/mysite/data/csv/bm_list.csv');
ig=importdata('/srv/vhosts/mysite/data/csv/ig_list.csv');
cg=importdata('/srv/vhosts/mysite/data/csv/cg_list.csv');
th=importdata('/srv/vhosts/mysite/data/csv/th_list.csv');
fn=importdata('/srv/vhosts/mysite/data/csv/fn_list.csv');
sl=importdata('/srv/vhosts/mysite/data/csv/shares_list.csv');

for l=2:2
    load(char(strcat('/srv/vhosts/mysite/matlab/data/bm/',bm(l),'_anfis.mat')))
end

for i=length(r_close_)-300:1:length(r_close_)
   data_=[r_close_(i-5) r_close_(i-4) r_close_(i-3) r_close_(i-2) r_close_(i-1)]; 
   foricast1(i) = evalfis(data_, fismat1);
   foricast2(i) = evalfis(data_, fismat2);
   real_r(i)=r_close_(i);

end

figure
subplot(211)
plot(foricast1,'.-g'); hold on; grid
plot(foricast2,'.-r')
plot(real_r,'.-')