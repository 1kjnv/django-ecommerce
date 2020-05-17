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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-04-27 21:19:42.045744','4','admin\'s cart',1,'[{\"added\": {}}]',9,5),(2,'2020-05-08 09:03:22.739624','9','Medical Stuff',1,'[{\"added\": {}}]',12,5),(3,'2020-05-08 09:03:33.599545','10','Software',1,'[{\"added\": {}}]',12,5),(4,'2020-05-08 09:03:51.222918','9','Medical Stuff',3,'',12,5),(5,'2020-05-08 09:03:51.256818','8','groceries',3,'',12,5),(6,'2020-05-08 09:03:51.259197','7','books',3,'',12,5),(7,'2020-05-08 09:03:51.261418','6','shoes',3,'',12,5),(8,'2020-05-08 09:03:51.262847','5','beauty',3,'',12,5),(9,'2020-05-08 09:03:51.263896','4','women clothes',3,'',12,5),(10,'2020-05-08 09:03:51.265207','3','men clothes',3,'',12,5),(11,'2020-05-08 09:03:51.266722','2','household',3,'',12,5),(12,'2020-05-08 09:03:51.267891','1','electronics',3,'',12,5),(13,'2020-05-08 09:04:28.557229','11','Electronics',1,'[{\"added\": {}}]',12,5),(14,'2020-05-08 09:04:44.079197','12','Men',1,'[{\"added\": {}}]',12,5),(15,'2020-05-08 09:04:47.575300','13','Women',1,'[{\"added\": {}}]',12,5),(16,'2020-05-08 09:04:57.444472','14','Shoes',1,'[{\"added\": {}}]',12,5),(17,'2020-05-08 09:05:00.366420','15','Books',1,'[{\"added\": {}}]',12,5),(18,'2020-05-08 09:33:37.083953','16','Beauty',1,'[{\"added\": {}}]',12,5),(19,'2020-05-08 09:46:08.322451','17','Household',1,'[{\"added\": {}}]',12,5),(20,'2020-05-08 09:56:15.065921','18','Fashion',1,'[{\"added\": {}}]',12,5),(21,'2020-05-08 09:57:08.695838','19','Groceries',1,'[{\"added\": {}}]',12,5),(22,'2020-05-08 09:57:45.205614','20','Kids',1,'[{\"added\": {}}]',12,5);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-17 17:20:12
