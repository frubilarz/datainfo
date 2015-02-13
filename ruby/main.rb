include Math

# Calcula pi utilizando el algoritmo de Gauss-Legendre
def pi_gauss_legendre(an, bn, tn, pn)
  ann = (an + bn) / 2
  bnn = Math.sqrt(an * bn)
  tnn = tn - pn * ((an - ann) ** 2)
  pnn = 2 * pn

  pi = ((ann + bnn) ** 2) / (4 * tnn)

  return [pi, ann, bnn, tnn, pnn]
end

if __FILE__ == $0
  # Valores iniciales del algoritmo de Gauss-Legendre
  an = 1.0
  bn = 1 / (Math.sqrt(2))
  tn = 1 / 4.0
  pn = 1.0

  # Cantidad de iteraciones del algoritmo
  iters = 10
  (1..iters).each do |n|
    pi, an, bn, tn, pn = pi_gauss_legendre(an, bn, tn, pn)
    puts 'pi(iter=%d) = %s (an = %f; bn = %f, tn = %f, pn = %f)' % [n, pi, an, bn, tn, pn]
  end
end

