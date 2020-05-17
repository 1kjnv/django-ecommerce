-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-04-24 16:19:39.540018'),(2,'auth','0001_initial','2020-04-24 16:19:39.621918'),(3,'admin','0001_initial','2020-04-24 16:19:39.822090'),(4,'admin','0002_logentry_remove_auto_add','2020-04-24 16:19:39.867340'),(5,'admin','0003_logentry_add_action_flag_choices','2020-04-24 16:19:39.875888'),(6,'contenttypes','0002_remove_content_type_name','2020-04-24 16:19:39.941107'),(7,'auth','0002_alter_permission_name_max_length','2020-04-24 16:19:39.969762'),(8,'auth','0003_alter_user_email_max_length','2020-04-24 16:19:39.991503'),(9,'auth','0004_alter_user_username_opts','2020-04-24 16:19:40.002433'),(10,'auth','0005_alter_user_last_login_null','2020-04-24 16:19:40.030877'),(11,'auth','0006_require_contenttypes_0002','2020-04-24 16:19:40.033663'),(12,'auth','0007_alter_validators_add_error_messages','2020-04-24 16:19:40.044096'),(13,'auth','0008_alter_user_username_max_length','2020-04-24 16:19:40.084641'),(14,'auth','0009_alter_user_last_name_max_length','2020-04-24 16:19:40.123837'),(15,'auth','0010_alter_group_name_max_length','2020-04-24 16:19:40.140537'),(16,'auth','0011_update_proxy_permissions','2020-04-24 16:19:40.151329'),(17,'backend','0001_initial','2020-04-24 16:19:40.198446'),(18,'cart','0001_initial','2020-04-24 16:19:40.277810'),(19,'sessions','0001_initial','2020-04-24 16:19:40.355446'),(20,'backend','0002_contact','2020-04-28 04:14:08.671907'),(21,'backend','0003_category','2020-05-03 08:59:26.581289'),(22,'backend','0004_auto_20200503_0900','2020-05-03 09:42:33.074698'),(23,'backend','0005_auto_20200503_0939','2020-05-03 09:42:33.110004'),(24,'backend','0006_auto_20200503_0939','2020-05-03 09:42:33.137544'),(25,'backend','0007_remove_item_category','2020-05-03 09:42:33.204622'),(26,'backend','0002_item_category','2020-05-04 08:55:20.751937'),(27,'backend','0003_auto_20200504_1533','2020-05-04 15:33:41.154649'),(28,'backend','0004_auto_20200508_0859','2020-05-08 08:59:38.009079'),(29,'ipn','0001_initial','2020-05-10 15:30:31.306162'),(30,'ipn','0002_paypalipn_mp_id','2020-05-10 15:30:31.399533'),(31,'ipn','0003_auto_20141117_1647','2020-05-10 15:30:31.492547'),(32,'ipn','0004_auto_20150612_1826','2020-05-10 15:30:32.618355'),(33,'ipn','0005_auto_20151217_0948','2020-05-10 15:30:32.678079'),(34,'ipn','0006_auto_20160108_1112','2020-05-10 15:30:32.832773'),(35,'ipn','0007_auto_20160219_1135','2020-05-10 15:30:32.851750'),(36,'ipn','0008_auto_20181128_1032','2020-05-10 15:30:32.872126'),(37,'backend','0002_order','2020-05-11 07:59:20.865067'),(38,'backend','0003_auto_20200511_0801','2020-05-11 08:01:31.977562'),(39,'backend','0004_order_price','2020-05-11 08:03:33.467303'),(40,'backend','0005_order_totalprice','2020-05-11 14:58:47.773714'),(41,'backend','0006_remove_order_address','2020-05-11 15:01:34.219465');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-17 17:20:13
