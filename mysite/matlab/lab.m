%importdata(shares_csv.csv)
clear; clc
bm=importdata('/srv/vhosts/mysite/data/csv/bm_list.csv');
ig=importdata('/srv/vhosts/mysite/data/csv/ig_list.csv');
cg=importdata('/srv/vhosts/mysite/data/csv/cg_list.csv');
th=importdata('/srv/vhosts/mysite/data/csv/th_list.csv');
fn=importdata('/srv/vhosts/mysite/data/csv/fn_list.csv');
sl=importdata('/srv/vhosts/mysite/data/csv/shares_list.csv');
  
 %   var = 'I_am looking for_the answer_here 5.';
 %   a= (regexp (var, ' ', 'split'));

 
 %name='/srv/vhosts/mysite/matlab/data/bm';
 %eval(['!mkdir ' name]);
   
 for l=1:12
    bm(l)
   %name=char(strcat('/srv/vhosts/mysite/matlab/data/bm/',bm(l)));
   %eval(['!mkdir ' name]);
   
   pt=importdata(char(strcat('/srv/vhosts/mysite/data/csv/',bm(l),'.csv')));
   p=pt.data;
   t=pt.textdata(2:end,1);
   p_open= p(1:end,1);
   p_max=  p(1:end,2);
   p_min=  p(1:end,3);
   p_close=p(1:end,4);
   volume= p(1:end,5);
   r_close=[0;price2ret(p_close)];
   for i=1:length(r_close);
       r_close_(i)=r_close(i);
       if  r_close(i)>0.3; r_close_(i)=0.3; end
       if  r_close(i)<-0.3; r_close_(i)=-0.3; end
   end

   figure
   subplot(2,1,1)
   plot(r_close); hold on
   plot(r_close_,'g');
   subplot(2,1,2)
   hist(r_close)
   
   for i=9:(length(r_close)-200)
       data_(i-8,:)=[r_close_(i-5) r_close_(i-4) r_close_(i-3) r_close_(i-2) r_close_(i-1) r_close_(i)]; 
   end
   trnData=data_(1:(length(data_)*0.9), :);
   chkData=data_((length(data_)*0.9+1):end, :);
   
   
   fismat = genfis1(trnData);
   
  
   
   [fismat1,error1,ss,fismat2,error2] = anfis(trnData,fismat,[],[],chkData);
   
 
   
   figure
   plot([error1 error2]);
   hold on; plot([error1 error2], 'o');
   xlabel('Epochs');
   ylabel('RMSE (Root Mean Squared Error)');
   title('Error Curves');
   
   save(char(strcat('/srv/vhosts/mysite/matlab/data/bm/',bm(l),'_anfis.mat')), 'fismat1', 'fismat2', 'p', 't', 'p_open', 'p_max', 'p_min', 'p_close', 'r_close', 'r_close_', 'volume')
 end
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 