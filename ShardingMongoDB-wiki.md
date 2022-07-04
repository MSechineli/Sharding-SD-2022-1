![Ficheiro:MongoDB Logo.svg – Wikipédia, a enciclopédia livre](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/MongoDB_Logo.svg/2560px-MongoDB_Logo.svg.png)

### Introdução

Sistemas de banco de dados com grandes conjuntos de dados ou aplicativos com alto rendimento podem desafiar a capacidade de um único servidor, já que muitas consultas sendo executadas ao mesmo tempo, geram um uso alto de processamento e de RAM. Para isso, existem dois métodos para abordar o crescimento do sistema, sendo eles: ***Vertical Scaling* (Escala vertical)** e ***Horizontal Scaling* (Escala Horizontal)**.

### *Vertical Scaling* (Escala vertical)

Envolve o aumento da capacidade de um único servidor, adicionando um processador mais potente, ou adicionando mais RAM, ou também adicionando mais capacidade de armazenamento. No entanto, isto há limitações, impedindo que uma única máquina seja suficientemente poderosa para uma determinada carga de trabalho, ou seja, há um máximo prático para a escala vertical.

### ***Horizontal Scaling* (Escala Horizontal)**

Envolve a divisão do conjunto de dados do sistema em vários servidores, adicionando servidores para aumentar a capacidade conforme o necessário. A expansão da capacidade da implantação requer apenas a adição de servidores, gerando um custo menor do que um hardware de ponta para uma única máquina. Mesmo que a velocidade ou capacidade de uma única máquina possa não ser alta, cada máquina lida com um subconjunto da carga de trabalho geral, fornecendo assim melhor eficiência do que um único servidor.

### O que é Sharding e como funciona no MongoDB?

O MongoDB fornece a funcionalidade sharding, que é um método para distribuir dados entre várias máquinas. Ele é utilizado para dar suporte a implantações em conjunto grande de dados e operações de alto rendimento.

No MongoDB, temos um cluster composto por três componentes:

* **shard:** Cada shard possui um subconjunto dos dados fragmentados. Cada shard também pode ser implantado como um conjunto de réplicas.
* **mongos:** Atua como roteador de consulta, fornecendo uma interface entre os aplicativos cliente e o shard cluster.
* **config-servers:** Os servidores de configuração armazenam metadados e definições de configuração para o cluster.

A imagem a seguir mostra a interação dos componentes em um shard cluster:

![Diagrama de um cluster fragmentado de amostra para fins de produção.  Contém exatamente 3 servidores de configuração, 2 ou mais roteadores de consulta ``mongos`` e pelo menos 2 shards.  Os fragmentos são conjuntos de réplicas.](https://www.mongodb.com/docs/manual/images/sharded-cluster-production-architecture.bakedsvg.svg)

Para que os dados sejam distribuídos para cada shard, o MongoDB utiliza uma chave de fragmentação, sendo uma etapa muito importante no processo de sharding, já que a chave de fragmentação ideal, permite que o MongoDB distribua os dados uniformemente por todo o cluster e facilita os padrões de consulta. Pode-se dizer que a chave de fragmentação por hash é a que fornece uma distribuição de dados mais uniforme, especialmente em dados que a chave de fragmentação muda monotonicamente (neste caso, a chave pode ter valores com altas variações).

### Vantagens do sharding

* **Capacidade de armazenamento:** O sharding distribui os dados entre os shards localizados no cluster, dessa forma, cada shard do cluster contém um subconjunto do total de dados. À medida que o conjunto de dados cresce, os shards adicionais aumentam a capacidade de armazenamento do cluster.
* **Alta disponibilidade:** A implantação de servidores de configuração e shards como conjuntos de réplicas oferece maior disponibilidade. Mesmo se um ou mais conjuntos de réplicas ficarem indisponíveis, o shard-cluster poderá continuar a realizar suas leituras e escritas parciais.

### Conclusão

O sharding tem sido amplamente utilizado como uma estratégia para melhorar o desempenho e a escalabilidade de grandes clusters de dados. Quando combinado com a replicação, a fragmentação também tem o potencial de melhorar a disponibilidade e a segurança dos dados. O sharding também é o principal meio de dimensionamento horizontal do MongoDB, pois você pode estender o desempenho do cluster de banco de dados adicionando mais nós ao cluster em vez de migrar bancos de dados para servidores maiores e mais poderosos.

### Referências

MONGODB. **MongoDB Documentation.** 2022. Disponível em: https://www.mongodb.com/docs/manual/sharding/#learn-more. Acesso em: 1 jul. 2022.

PAPIERNIK, Mateusz; DRAKE, Mark. **How To Use Sharding in MongoDB.** 21 dez. 2021. artigo. P&B. Disponível em: https://www.digitalocean.com/community/tutorials/how-to-use-sharding-in-mongodb. Acesso em: 1 jul. 2022.















