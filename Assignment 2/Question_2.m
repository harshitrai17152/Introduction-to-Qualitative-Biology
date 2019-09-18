%% 
% Harshit Rai
% 2017152

%% Initial equation

clear all;
clc;

syms p q;
p1=p*(1+(1.3)*(1-p))-(0.5)*p*q;   % Given equations
q1=(0.3)*q+(1.6)*p*q;

%% Stable Points
    
syms p q;
[solx,soly]=solve( p==p*(1+(1.3)*(1-p))-(0.5)*p*q , q==(0.3)*q+(1.6)*p*q );    % Function to solve the linear difference equation
display('Stable Points');
[solx,soly]

%% Partial diffrentiation

syms a b c d;
a=diff(p1,p);    % function to diffrentiate a function with respect to a variable
b=diff(q1,p);
c=diff(p1,q);
d=diff(q1,q);

%% Jacobian

a1=subs(a,{p,q},{0.4375,1.4625});      % Putting the given points in this Jacobian matrix
b1=subs(b,{p,q},{0.4375,1.4625});
c1=subs(c,{p,q},{0.4375,1.4625});
d1=subs(d,{p,q},{0.4375,1.4625});

J=[a c ; b d];
display('Jacobian');
J

%% Steady State Plot

syms p q;
[solx,soly]=solve( p==p*(1+(1.3)*(1-p))-(0.5)*p*q , q==(0.3)*q+(1.6)*p*q );     
a=[solx,soly];

display('Steady State Plot')
plot(a(1,1),a(1,2),'*',a(2,1),a(2,2),'*',a(3,1),a(3,2),'*');
figure()

%% Phase Plane Plot and Time Series Plot

n=20;
p=1.10;
q=0.40;

prey=zeros(1,n);    
predator=zeros(1,n);
prey(1)=p;
predator(1)=q;

for i=1:n-1
    
    x=p*(1+(1.3)*(1-p))-(0.5)*p*q;           % Discrete time equation 'Delte P=P(t+1)-p(t)'
    y=(0.3)*q+(1.6)*p*q;
    
    prey(i+1)=x;                    
    predator(i+1)=y;   
    
    p=x;
    q=y;

end

t=1:1:n;

plot(t,prey,'Color','r');
hold on;   
plot(t,predator,'Color','k');
title('Time Series Plot');
ylabel('Population \rightarrow');
xlabel('Time \rightarrow');
legend('Prey population','Predator population');

figure;
plot(prey,predator);                     
title('Phase Plane Plot');
xlabel('Prey Population \rightarrow');
ylabel('Predator population \rightarrow');

%% Eigen Vectors and eigen values

pro=[a1 c1 ; b1 d1];      % Projection Matrix
display('Eigen vectors');
eig(pro)

%% Stability

display('It is an Unstable Dynamics because absolute value of both the eigenvalues is greater than 1')

