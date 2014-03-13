function runrandom(subject, cond, st, fin)
disp(st)
class(st)
links_file = ['/mnt/tier2/urihas/Andric/steadystate/links_files5p/',subject,'.',cond,'.5p_r0.5_linksthresh_proportion.out.links'];
disp(links_file)
edgelist=dlmread(links_file);
disp(size(edgelist))
edgelist=edgelist(:,1:2);
adjmat=zeros(max(max(edgelist+1)),'uint8');
for i=1:length(edgelist)
    adjmat(1+edgelist(i,1),1+edgelist(i,2))=1;
end
adjmat=adjmat+adjmat';
i = st;
while(i < fin)
    tic; randmat=sym_generate_srand(adjmat); 
    [Ci Q] = modularity_louvain_und(randmat); toc
    dlmwrite(['/mnt/tier2/urihas/Andric/steadystate/links_files5p/rando/rand_',num2str(i),'_',subject,'_',cond,'.Q'], Q);
    i = i + 1;
end

