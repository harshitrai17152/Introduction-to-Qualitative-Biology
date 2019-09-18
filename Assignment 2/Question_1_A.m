%% 
% Harshit Rai
% 2017152

                                                % Part A

clear all;
clc;

%% Equillibrium Points

syms x y;
[solx,soly]=solve( x==3*x , y==x+2*y );    % Function to solve the linear difference equation
display('Equillibrium points');
[solx,soly]

%% Eigenvectors and Eigenvalues

a=[3 0;1 2];  % Projection matrix
[V,L]=eig(a);             % Function to find eigenvalue and eigenvectors
display('Eigen vectors');
V(:,1)
V(:,2)
display('Eigen values');
L(1,1)
L(2,2)

%% Eigenvector Plot

quiver(0,0,V(1,2),V(2,2));  
hold on;
quiver(0,0,V(1,1),V(2,1))
title('Eigenvector Plot');
legend('Eigenvector 1','Eigenvector 2'); 

%% Direction field

[p,q]=meshgrid(-3:0.5:3,-3:0.5:3);
p1=2*p;
q1=p+q;

dy=p1;
dx=q1;

figure
quiver(p,q,p1,q1)
title('Direction Field');
legend('Direction Field'); 

%% Stability

display('It is an unstable Point')
    
    