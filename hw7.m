clear
for i=1:10
fprintf(strcat(num2str(i),' matrix:'))
fprintf('running time of Bregman divergence:')
A = rand(100,100);
tic
V = assbreg(A);
toc
obj_func = trace(A'*V);
fprintf(strcat('objective value:',num2str(obj_func)))
fprintf('\n')
fprintf('running time of LAPJV:')
B = -A;
tic
[rowsol,cost,v,u,costMat] = lapjv(B);
toc
fprintf(strcat('objective function:',num2str(-cost)))
fprintf('\n')
end