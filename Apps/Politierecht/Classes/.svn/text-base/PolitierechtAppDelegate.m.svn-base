//
//  PolitierechtAppDelegate.m
//  Politierecht
//
//  Created by rabshakeh on 9/28/09 - 3:10 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import "PolitierechtAppDelegate.h"
#import "PolitierechtViewController.h"
#import "TableViewFromDatabaseViewController.h"
#import "ArtikelViewControllerFromXIB.h"
#import "WetboekSearchViewController.h"

@implementation PolitierechtAppDelegate

@synthesize window ;
@synthesize viewController ;


-(void) applicationDidFinishLaunching: (UIApplication *) application
{
  TableViewFromDatabaseViewController *tableViewFromDatabaseController = [[TableViewFromDatabaseViewController alloc] init] ;

  tableViewFromDatabaseController.table_name = @"wetboekhoofdstuk" ;
  tableViewFromDatabaseController.next_table = @"wetboek" ;
  tableViewFromDatabaseController.title      = @"Politierecht - Apr. 2011" ;
  [tableViewFromDatabaseController reload] ;
  navigationController = [[UINavigationController alloc] initWithRootViewController:tableViewFromDatabaseController] ;

  [tableViewFromDatabaseController release] ;
  navigationController.navigationBar.tintColor = [UIColor colorWithRed:0.10196078431372549 green:0.14901960784313725 blue:0.25098039215686274 alpha:0] ;

  [window addSubview:[navigationController view]] ;

  [window makeKeyAndVisible] ;
}


-(void) dealloc
{
  [viewController release] ;
  [window release] ;
  [super dealloc] ;
}


@end
