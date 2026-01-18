
## An holistic approach

In this section, you will learn how to register information about your working environment inside database files. The first thing that you need to be aware is that this kind of information is not limited to microfading analyses. For example, we will register information about objects or researchers, knowing that several different types of analyses can be performed on objects by different researchers. Therefore, we need to have an holistic / global approach when registering such information. This is the reason why, such tasks are not performed by the `microfading` package, but by another package called [msdb](https://g-patin.github.io/msdb/) (material science database).


## MSDB package

The `msdb` package will allow you to create a set of simple csv and txt files inside which you will be able to record information about your working environment. Have a look at the documentation website of the `msdb` package and especially the [get started section](https://g-patin.github.io/msdb/get-started/). But the first thing you will need to do is to [create the database files](https://g-patin.github.io/msdb/create-databases/). Afterwards, you will be able to record information inside the database files ([msdb - add info](https://g-patin.github.io/msdb/databases-usage/)). The last step will be to connect the `microfading` package with the name of msdb database files that you just created (see section [Connect with db files](https://g-patin.github.io/microfading/connection-db-files/)). This will enable the `microfading` package to have access to the information stored in the database files, so that they can automatically be added to your microfading analyses. More precisely, inside the *interim* microfading file, the values contained in first tab, called *info*, come from the information stored in the msdb database files. 

&nbsp;

To sum-up, just follow the steps:

1. [create](https://g-patin.github.io/msdb/create-databases/) the database files

2. [add info](https://g-patin.github.io/msdb/databases-usage/) inside the databases files

3. [connect](https://g-patin.github.io/microfading/connection-db-files/) the databases with the `microfading` package

---

© 2026 Gauthier Patin. All rights reserved. | Last updated: 2026-01-18

