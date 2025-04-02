import euler_de as ed

rho, sigma, beta = 28, 10, 8/3

x_dash = lambda t,x,y,z: sigma*(y-x)
y_dash = lambda t,x,y,z: x*(rho-z) - y
z_dash = lambda t,x,y,z: x*y - beta*z

z0 = 0
y0 = 0
x0 = 0.99 ## Non-zero initial value
t0 = 0

h = 0.01
tn = 20

initial_condition = (z0,y0,x0,t0)
diff_equations = (z_dash, y_dash, x_dash)
integration_settings = (h,tn)

solution = ed.euler_de(diff_equations, initial_condition, integration_settings)

z, y, x, t = solution


